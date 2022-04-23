
import asyncio
import functools
import logging
import sys

import rospy

logger = logging.getLogger(__name__)


class AsyncServiceProxy:

    def __init__(self, name, service_class):
        self.name = name
        self.service_class = service_class
        self._loop = asyncio.get_event_loop()
        self._lock = asyncio.Lock()
        self._srv_proxy = rospy.ServiceProxy(name, service_class)

    async def wait_for_service(self):
        """ Wait for a ROS service to be available. """
        await self._wait_for_service()

    async def _wait_for_service(self):
        while True:
            try:
                # ~Use a small timeout so the execution can be cancelled if necessary~
                # Use a large timeout, otherwise wait_for_service will never succeed in bad networking environments.
                return await self._loop.run_in_executor(None, self._srv_proxy.wait_for_service, 10.0)
            except rospy.ROSException:
                continue

    async def send(self, *args, **kwargs):
        """ Send a request to a ROS service. """
        log_period = kwargs.pop('log_period', None)
        service_call = functools.partial(self._srv_proxy.call, *args, **kwargs)
        # Non-persistent ServiceProxy is not thread safe
        # https://github.com/ros/ros_comm/blob/noetic-devel/clients/rospy/src/rospy/impl/tcpros_service.py#L534
        async with self._lock:
            return await self._loop.run_in_executor(None, service_call)

    async def ensure(self, *args, **kwargs):
        """ Send a request to a ROS service, retrying if comms failure is detected. """
        while True:
            await self.wait_for_service()
            try:
                return await self.send(*args, **kwargs)
            except (rospy.ServiceException, AttributeError, rospy.exceptions.ROSException,
                    rospy.exceptions.ROSInternalException) as e:
                logger.exception(f"Caught exception {e}, retrying service call...")
                continue

