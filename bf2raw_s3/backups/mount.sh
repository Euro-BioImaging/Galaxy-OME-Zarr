#rclone --config /home/oezdemir/PycharmProjects/rclone/mount_s3/.rclone.conf mount minio:eosc-future /home/oezdemir/PycharmProjects/rclone/s3mount
rclone --config $__tool_directory__/.rclone.conf mount minio:$1 $2

