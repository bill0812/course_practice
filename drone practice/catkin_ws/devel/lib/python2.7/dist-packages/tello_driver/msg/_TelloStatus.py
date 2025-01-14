# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from tello_driver/TelloStatus.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class TelloStatus(genpy.Message):
  _md5sum = "e6d1629583c9b3a337a806afc71e19f7"
  _type = "tello_driver/TelloStatus"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """# Non-negative; calibrated to takeoff altitude; auto-calib if falls below takeoff height; inaccurate near ground
float32 height_m

float32 speed_northing_mps
float32 speed_easting_mps
float32 speed_horizontal_mps
float32 speed_vertical_mps

float32 flight_time_sec

bool imu_state
bool pressure_state
bool down_visual_state
bool power_state
bool battery_state
bool gravity_state
bool wind_state

uint8 imu_calibration_state
uint8 battery_percentage
float32 drone_fly_time_left_sec
float32 drone_battery_left_sec

bool is_flying
bool is_on_ground
# is_em_open True in flight, False when landed
bool is_em_open
bool is_drone_hover
bool is_outage_recording
bool is_battery_low
bool is_battery_lower
bool is_factory_mode

# flymode=1: landed; =6: flying
uint8 fly_mode
float32 throw_takeoff_timer_sec
uint8 camera_state

uint8 electrical_machinery_state

bool front_in
bool front_out
bool front_lsc

float32 temperature_height_m

float32 cmd_roll_ratio
float32 cmd_pitch_ratio
float32 cmd_yaw_ratio
float32 cmd_vspeed_ratio
bool cmd_fast_mode"""
  __slots__ = ['height_m','speed_northing_mps','speed_easting_mps','speed_horizontal_mps','speed_vertical_mps','flight_time_sec','imu_state','pressure_state','down_visual_state','power_state','battery_state','gravity_state','wind_state','imu_calibration_state','battery_percentage','drone_fly_time_left_sec','drone_battery_left_sec','is_flying','is_on_ground','is_em_open','is_drone_hover','is_outage_recording','is_battery_low','is_battery_lower','is_factory_mode','fly_mode','throw_takeoff_timer_sec','camera_state','electrical_machinery_state','front_in','front_out','front_lsc','temperature_height_m','cmd_roll_ratio','cmd_pitch_ratio','cmd_yaw_ratio','cmd_vspeed_ratio','cmd_fast_mode']
  _slot_types = ['float32','float32','float32','float32','float32','float32','bool','bool','bool','bool','bool','bool','bool','uint8','uint8','float32','float32','bool','bool','bool','bool','bool','bool','bool','bool','uint8','float32','uint8','uint8','bool','bool','bool','float32','float32','float32','float32','float32','bool']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       height_m,speed_northing_mps,speed_easting_mps,speed_horizontal_mps,speed_vertical_mps,flight_time_sec,imu_state,pressure_state,down_visual_state,power_state,battery_state,gravity_state,wind_state,imu_calibration_state,battery_percentage,drone_fly_time_left_sec,drone_battery_left_sec,is_flying,is_on_ground,is_em_open,is_drone_hover,is_outage_recording,is_battery_low,is_battery_lower,is_factory_mode,fly_mode,throw_takeoff_timer_sec,camera_state,electrical_machinery_state,front_in,front_out,front_lsc,temperature_height_m,cmd_roll_ratio,cmd_pitch_ratio,cmd_yaw_ratio,cmd_vspeed_ratio,cmd_fast_mode

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(TelloStatus, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.height_m is None:
        self.height_m = 0.
      if self.speed_northing_mps is None:
        self.speed_northing_mps = 0.
      if self.speed_easting_mps is None:
        self.speed_easting_mps = 0.
      if self.speed_horizontal_mps is None:
        self.speed_horizontal_mps = 0.
      if self.speed_vertical_mps is None:
        self.speed_vertical_mps = 0.
      if self.flight_time_sec is None:
        self.flight_time_sec = 0.
      if self.imu_state is None:
        self.imu_state = False
      if self.pressure_state is None:
        self.pressure_state = False
      if self.down_visual_state is None:
        self.down_visual_state = False
      if self.power_state is None:
        self.power_state = False
      if self.battery_state is None:
        self.battery_state = False
      if self.gravity_state is None:
        self.gravity_state = False
      if self.wind_state is None:
        self.wind_state = False
      if self.imu_calibration_state is None:
        self.imu_calibration_state = 0
      if self.battery_percentage is None:
        self.battery_percentage = 0
      if self.drone_fly_time_left_sec is None:
        self.drone_fly_time_left_sec = 0.
      if self.drone_battery_left_sec is None:
        self.drone_battery_left_sec = 0.
      if self.is_flying is None:
        self.is_flying = False
      if self.is_on_ground is None:
        self.is_on_ground = False
      if self.is_em_open is None:
        self.is_em_open = False
      if self.is_drone_hover is None:
        self.is_drone_hover = False
      if self.is_outage_recording is None:
        self.is_outage_recording = False
      if self.is_battery_low is None:
        self.is_battery_low = False
      if self.is_battery_lower is None:
        self.is_battery_lower = False
      if self.is_factory_mode is None:
        self.is_factory_mode = False
      if self.fly_mode is None:
        self.fly_mode = 0
      if self.throw_takeoff_timer_sec is None:
        self.throw_takeoff_timer_sec = 0.
      if self.camera_state is None:
        self.camera_state = 0
      if self.electrical_machinery_state is None:
        self.electrical_machinery_state = 0
      if self.front_in is None:
        self.front_in = False
      if self.front_out is None:
        self.front_out = False
      if self.front_lsc is None:
        self.front_lsc = False
      if self.temperature_height_m is None:
        self.temperature_height_m = 0.
      if self.cmd_roll_ratio is None:
        self.cmd_roll_ratio = 0.
      if self.cmd_pitch_ratio is None:
        self.cmd_pitch_ratio = 0.
      if self.cmd_yaw_ratio is None:
        self.cmd_yaw_ratio = 0.
      if self.cmd_vspeed_ratio is None:
        self.cmd_vspeed_ratio = 0.
      if self.cmd_fast_mode is None:
        self.cmd_fast_mode = False
    else:
      self.height_m = 0.
      self.speed_northing_mps = 0.
      self.speed_easting_mps = 0.
      self.speed_horizontal_mps = 0.
      self.speed_vertical_mps = 0.
      self.flight_time_sec = 0.
      self.imu_state = False
      self.pressure_state = False
      self.down_visual_state = False
      self.power_state = False
      self.battery_state = False
      self.gravity_state = False
      self.wind_state = False
      self.imu_calibration_state = 0
      self.battery_percentage = 0
      self.drone_fly_time_left_sec = 0.
      self.drone_battery_left_sec = 0.
      self.is_flying = False
      self.is_on_ground = False
      self.is_em_open = False
      self.is_drone_hover = False
      self.is_outage_recording = False
      self.is_battery_low = False
      self.is_battery_lower = False
      self.is_factory_mode = False
      self.fly_mode = 0
      self.throw_takeoff_timer_sec = 0.
      self.camera_state = 0
      self.electrical_machinery_state = 0
      self.front_in = False
      self.front_out = False
      self.front_lsc = False
      self.temperature_height_m = 0.
      self.cmd_roll_ratio = 0.
      self.cmd_pitch_ratio = 0.
      self.cmd_yaw_ratio = 0.
      self.cmd_vspeed_ratio = 0.
      self.cmd_fast_mode = False

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_get_struct_6f9B2f9Bf5B5fB().pack(_x.height_m, _x.speed_northing_mps, _x.speed_easting_mps, _x.speed_horizontal_mps, _x.speed_vertical_mps, _x.flight_time_sec, _x.imu_state, _x.pressure_state, _x.down_visual_state, _x.power_state, _x.battery_state, _x.gravity_state, _x.wind_state, _x.imu_calibration_state, _x.battery_percentage, _x.drone_fly_time_left_sec, _x.drone_battery_left_sec, _x.is_flying, _x.is_on_ground, _x.is_em_open, _x.is_drone_hover, _x.is_outage_recording, _x.is_battery_low, _x.is_battery_lower, _x.is_factory_mode, _x.fly_mode, _x.throw_takeoff_timer_sec, _x.camera_state, _x.electrical_machinery_state, _x.front_in, _x.front_out, _x.front_lsc, _x.temperature_height_m, _x.cmd_roll_ratio, _x.cmd_pitch_ratio, _x.cmd_yaw_ratio, _x.cmd_vspeed_ratio, _x.cmd_fast_mode))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      end = 0
      _x = self
      start = end
      end += 80
      (_x.height_m, _x.speed_northing_mps, _x.speed_easting_mps, _x.speed_horizontal_mps, _x.speed_vertical_mps, _x.flight_time_sec, _x.imu_state, _x.pressure_state, _x.down_visual_state, _x.power_state, _x.battery_state, _x.gravity_state, _x.wind_state, _x.imu_calibration_state, _x.battery_percentage, _x.drone_fly_time_left_sec, _x.drone_battery_left_sec, _x.is_flying, _x.is_on_ground, _x.is_em_open, _x.is_drone_hover, _x.is_outage_recording, _x.is_battery_low, _x.is_battery_lower, _x.is_factory_mode, _x.fly_mode, _x.throw_takeoff_timer_sec, _x.camera_state, _x.electrical_machinery_state, _x.front_in, _x.front_out, _x.front_lsc, _x.temperature_height_m, _x.cmd_roll_ratio, _x.cmd_pitch_ratio, _x.cmd_yaw_ratio, _x.cmd_vspeed_ratio, _x.cmd_fast_mode,) = _get_struct_6f9B2f9Bf5B5fB().unpack(str[start:end])
      self.imu_state = bool(self.imu_state)
      self.pressure_state = bool(self.pressure_state)
      self.down_visual_state = bool(self.down_visual_state)
      self.power_state = bool(self.power_state)
      self.battery_state = bool(self.battery_state)
      self.gravity_state = bool(self.gravity_state)
      self.wind_state = bool(self.wind_state)
      self.is_flying = bool(self.is_flying)
      self.is_on_ground = bool(self.is_on_ground)
      self.is_em_open = bool(self.is_em_open)
      self.is_drone_hover = bool(self.is_drone_hover)
      self.is_outage_recording = bool(self.is_outage_recording)
      self.is_battery_low = bool(self.is_battery_low)
      self.is_battery_lower = bool(self.is_battery_lower)
      self.is_factory_mode = bool(self.is_factory_mode)
      self.front_in = bool(self.front_in)
      self.front_out = bool(self.front_out)
      self.front_lsc = bool(self.front_lsc)
      self.cmd_fast_mode = bool(self.cmd_fast_mode)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_get_struct_6f9B2f9Bf5B5fB().pack(_x.height_m, _x.speed_northing_mps, _x.speed_easting_mps, _x.speed_horizontal_mps, _x.speed_vertical_mps, _x.flight_time_sec, _x.imu_state, _x.pressure_state, _x.down_visual_state, _x.power_state, _x.battery_state, _x.gravity_state, _x.wind_state, _x.imu_calibration_state, _x.battery_percentage, _x.drone_fly_time_left_sec, _x.drone_battery_left_sec, _x.is_flying, _x.is_on_ground, _x.is_em_open, _x.is_drone_hover, _x.is_outage_recording, _x.is_battery_low, _x.is_battery_lower, _x.is_factory_mode, _x.fly_mode, _x.throw_takeoff_timer_sec, _x.camera_state, _x.electrical_machinery_state, _x.front_in, _x.front_out, _x.front_lsc, _x.temperature_height_m, _x.cmd_roll_ratio, _x.cmd_pitch_ratio, _x.cmd_yaw_ratio, _x.cmd_vspeed_ratio, _x.cmd_fast_mode))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      end = 0
      _x = self
      start = end
      end += 80
      (_x.height_m, _x.speed_northing_mps, _x.speed_easting_mps, _x.speed_horizontal_mps, _x.speed_vertical_mps, _x.flight_time_sec, _x.imu_state, _x.pressure_state, _x.down_visual_state, _x.power_state, _x.battery_state, _x.gravity_state, _x.wind_state, _x.imu_calibration_state, _x.battery_percentage, _x.drone_fly_time_left_sec, _x.drone_battery_left_sec, _x.is_flying, _x.is_on_ground, _x.is_em_open, _x.is_drone_hover, _x.is_outage_recording, _x.is_battery_low, _x.is_battery_lower, _x.is_factory_mode, _x.fly_mode, _x.throw_takeoff_timer_sec, _x.camera_state, _x.electrical_machinery_state, _x.front_in, _x.front_out, _x.front_lsc, _x.temperature_height_m, _x.cmd_roll_ratio, _x.cmd_pitch_ratio, _x.cmd_yaw_ratio, _x.cmd_vspeed_ratio, _x.cmd_fast_mode,) = _get_struct_6f9B2f9Bf5B5fB().unpack(str[start:end])
      self.imu_state = bool(self.imu_state)
      self.pressure_state = bool(self.pressure_state)
      self.down_visual_state = bool(self.down_visual_state)
      self.power_state = bool(self.power_state)
      self.battery_state = bool(self.battery_state)
      self.gravity_state = bool(self.gravity_state)
      self.wind_state = bool(self.wind_state)
      self.is_flying = bool(self.is_flying)
      self.is_on_ground = bool(self.is_on_ground)
      self.is_em_open = bool(self.is_em_open)
      self.is_drone_hover = bool(self.is_drone_hover)
      self.is_outage_recording = bool(self.is_outage_recording)
      self.is_battery_low = bool(self.is_battery_low)
      self.is_battery_lower = bool(self.is_battery_lower)
      self.is_factory_mode = bool(self.is_factory_mode)
      self.front_in = bool(self.front_in)
      self.front_out = bool(self.front_out)
      self.front_lsc = bool(self.front_lsc)
      self.cmd_fast_mode = bool(self.cmd_fast_mode)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_6f9B2f9Bf5B5fB = None
def _get_struct_6f9B2f9Bf5B5fB():
    global _struct_6f9B2f9Bf5B5fB
    if _struct_6f9B2f9Bf5B5fB is None:
        _struct_6f9B2f9Bf5B5fB = struct.Struct("<6f9B2f9Bf5B5fB")
    return _struct_6f9B2f9Bf5B5fB
