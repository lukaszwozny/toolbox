import os
import appdirs

# TEMP_DIR = os.path.join(
#     appdirs.user_data_dir(),
#     "toolbox-git",
# )

TEMP_DIR = "toolbox-git"


def build_temp_dir(dir):
    return os.path.join(
        appdirs.user_data_dir(),
        dir,
    )
