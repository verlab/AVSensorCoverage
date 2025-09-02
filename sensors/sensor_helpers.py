import yaml
from easydict import EasyDict as edict

from .camera import Camera
from .lidar import Lidar
from .radar import Radar
from .sonar import Sonar


def load_sensorset(yaml_file):
    with open(yaml_file, 'r') as file:
        yaml_sensors = yaml.safe_load(file)
    sensor_definition = edict(yaml_sensors)

    sensor_list = []
    if hasattr(sensor_definition, 'cameras'):
        for camera_data in sensor_definition['cameras']:
            obj_camera = Camera(
                position=[
                    camera_data.position.x,
                    camera_data.position.y,
                    camera_data.position.z
                ],
                fov=camera_data.fov,
                max_dist=camera_data.max_dist,
                min_dist=camera_data.min_dist,
                image_width=camera_data.n_pixels.width,
                image_height=camera_data.n_pixels.height,
                name=camera_data.name
            )
            obj_camera.rotate(
                pitch=camera_data.orientation.pitch,
                yaw=camera_data.orientation.yaw,
                roll=camera_data.orientation.roll,
            )
            sensor_list.append(obj_camera)

    if hasattr(sensor_definition, 'lidars'):
        for lidar_data in sensor_definition['lidars']:
            obj_lidar = Lidar(
                position=[
                    lidar_data.position.x,
                    lidar_data.position.y,
                    lidar_data.position.z
                ],
                fov_h=lidar_data.fov_h,
                fov_v=lidar_data.fov_v,
                detection_range=lidar_data.detection_range,
                min_range=lidar_data.min_range,
                name=lidar_data.name,
            )
            obj_lidar.rotate(
                pitch=lidar_data.orientation.pitch,
                yaw=lidar_data.orientation.yaw,
                roll=lidar_data.orientation.roll,
            )
            sensor_list.append(obj_lidar)

    if hasattr(sensor_definition, 'radars'):
        for radar_data in sensor_definition['radars']:
            obj_radar = Radar(
                position=[
                    radar_data.position.x,
                    radar_data.position.y,
                    radar_data.position.z
                ],
                fov_h=radar_data.fov_h,
                fov_v=radar_data.fov_v,
                detection_range=radar_data.detection_range,
                min_range=radar_data.min_range,
                name=radar_data.name,
            )
            obj_radar.rotate(
                pitch=radar_data.orientation.pitch,
                yaw=radar_data.orientation.yaw,
                roll=radar_data.orientation.roll,
            )
            if hasattr(radar_data, 'offset'):
                obj_radar.translate(**radar_data.offset)
            sensor_list.append(obj_radar)
    
    if hasattr(sensor_definition, 'sonars'):
        for sonar_data in sensor_definition['sonars']:
            obj_sonar = Sonar(
                position=[
                    sonar_data.position.x,
                    sonar_data.position.y,
                    sonar_data.position.z
                ],
                fov_h=sonar_data.fov_h,
                fov_v=sonar_data.fov_v,
                detection_range=sonar_data.detection_range,
                min_range=sonar_data.min_range,
                name=sonar_data.name,
            )
            obj_sonar.rotate(
                pitch=sonar_data.orientation.pitch,
                yaw=sonar_data.orientation.yaw,
                roll=sonar_data.orientation.roll,
            )
            sensor_list.append(obj_sonar)

    return sensor_list
