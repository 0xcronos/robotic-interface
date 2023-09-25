import ikpy.chain
import numpy as np
import ikpy.utils.plot as plot_utils


braccio_chain = ikpy.chain.Chain.from_urdf_file("./urdf/braccio.urdf")
target_position = [0.001, 0, 0]

print("The angles of each joints are : ", braccio_chain.inverse_kinematics(target_position))

# real_frame = braccio_chain.forward_kinematics(braccio_chain.inverse_kinematics(target_position))
# print("Computed position vector : %s, original position vector : %s" % (real_frame[:3, 3], target_position))
