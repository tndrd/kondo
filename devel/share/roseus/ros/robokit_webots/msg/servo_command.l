;; Auto-generated. Do not edit!


(when (boundp 'robokit_webots::servo_command)
  (if (not (find-package "ROBOKIT_WEBOTS"))
    (make-package "ROBOKIT_WEBOTS"))
  (shadow 'servo_command (find-package "ROBOKIT_WEBOTS")))
(unless (find-package "ROBOKIT_WEBOTS::SERVO_COMMAND")
  (make-package "ROBOKIT_WEBOTS::SERVO_COMMAND"))

(in-package "ROS")
;;//! \htmlinclude servo_command.msg.html


(defclass robokit_webots::servo_command
  :super ros::object
  :slots (_names _values ))

(defmethod robokit_webots::servo_command
  (:init
   (&key
    ((:names __names) (let (r) (dotimes (i 0) (push "" r)) r))
    ((:values __values) (make-array 0 :initial-element 0.0 :element-type :float))
    )
   (send-super :init)
   (setq _names __names)
   (setq _values __values)
   self)
  (:names
   (&optional __names)
   (if __names (setq _names __names)) _names)
  (:values
   (&optional __values)
   (if __values (setq _values __values)) _values)
  (:serialization-length
   ()
   (+
    ;; string[] _names
    (apply #'+ (mapcar #'(lambda (x) (+ 4 (length x))) _names)) 4
    ;; float64[] _values
    (* 8    (length _values)) 4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string[] _names
     (write-long (length _names) s)
     (dolist (elem _names)
       (write-long (length elem) s) (princ elem s)
       )
     ;; float64[] _values
     (write-long (length _values) s)
     (dotimes (i (length _values))
       (sys::poke (elt _values i) (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
       )
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string[] _names
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _names (make-list n))
     (dotimes (i n)
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setf (elt _names i) (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
     ))
   ;; float64[] _values
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _values (instantiate float-vector n))
     (dotimes (i n)
     (setf (elt _values i) (sys::peek buf ptr- :double)) (incf ptr- 8)
     ))
   ;;
   self)
  )

(setf (get robokit_webots::servo_command :md5sum-) "d75ca66ca305927d9452c8ab1c55e95e")
(setf (get robokit_webots::servo_command :datatype-) "robokit_webots/servo_command")
(setf (get robokit_webots::servo_command :definition-)
      "string[] names
float64[] values

")



(provide :robokit_webots/servo_command "d75ca66ca305927d9452c8ab1c55e95e")


