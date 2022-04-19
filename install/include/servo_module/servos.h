// Generated by gencpp from file servo_module/servos.msg
// DO NOT EDIT!


#ifndef SERVO_MODULE_MESSAGE_SERVOS_H
#define SERVO_MODULE_MESSAGE_SERVOS_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace servo_module
{
template <class ContainerAllocator>
struct servos_
{
  typedef servos_<ContainerAllocator> Type;

  servos_()
    : names()
    , values()  {
    }
  servos_(const ContainerAllocator& _alloc)
    : names(_alloc)
    , values(_alloc)  {
  (void)_alloc;
    }



   typedef std::vector<std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > , typename ContainerAllocator::template rebind<std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > >::other >  _names_type;
  _names_type names;

   typedef std::vector<double, typename ContainerAllocator::template rebind<double>::other >  _values_type;
  _values_type values;





  typedef boost::shared_ptr< ::servo_module::servos_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::servo_module::servos_<ContainerAllocator> const> ConstPtr;

}; // struct servos_

typedef ::servo_module::servos_<std::allocator<void> > servos;

typedef boost::shared_ptr< ::servo_module::servos > servosPtr;
typedef boost::shared_ptr< ::servo_module::servos const> servosConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::servo_module::servos_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::servo_module::servos_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::servo_module::servos_<ContainerAllocator1> & lhs, const ::servo_module::servos_<ContainerAllocator2> & rhs)
{
  return lhs.names == rhs.names &&
    lhs.values == rhs.values;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::servo_module::servos_<ContainerAllocator1> & lhs, const ::servo_module::servos_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace servo_module

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsMessage< ::servo_module::servos_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::servo_module::servos_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::servo_module::servos_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::servo_module::servos_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::servo_module::servos_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::servo_module::servos_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::servo_module::servos_<ContainerAllocator> >
{
  static const char* value()
  {
    return "d75ca66ca305927d9452c8ab1c55e95e";
  }

  static const char* value(const ::servo_module::servos_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xd75ca66ca305927dULL;
  static const uint64_t static_value2 = 0x9452c8ab1c55e95eULL;
};

template<class ContainerAllocator>
struct DataType< ::servo_module::servos_<ContainerAllocator> >
{
  static const char* value()
  {
    return "servo_module/servos";
  }

  static const char* value(const ::servo_module::servos_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::servo_module::servos_<ContainerAllocator> >
{
  static const char* value()
  {
    return "string[] names\n"
"float64[] values\n"
;
  }

  static const char* value(const ::servo_module::servos_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::servo_module::servos_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.names);
      stream.next(m.values);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct servos_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::servo_module::servos_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::servo_module::servos_<ContainerAllocator>& v)
  {
    s << indent << "names[]" << std::endl;
    for (size_t i = 0; i < v.names.size(); ++i)
    {
      s << indent << "  names[" << i << "]: ";
      Printer<std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > >::stream(s, indent + "  ", v.names[i]);
    }
    s << indent << "values[]" << std::endl;
    for (size_t i = 0; i < v.values.size(); ++i)
    {
      s << indent << "  values[" << i << "]: ";
      Printer<double>::stream(s, indent + "  ", v.values[i]);
    }
  }
};

} // namespace message_operations
} // namespace ros

#endif // SERVO_MODULE_MESSAGE_SERVOS_H
