import os
import tensorflow as tf

num_skipped = 0
for folder_name in ("Cats", "Dogs"):
    folder_path = os.path.join("train", folder_name)
    for fname in os.listdir(folder_path):
        #print(fname)
        fpath = os.path.join(folder_path, fname)
        try:
            fobj = open(fpath, "rb")
            is_jfif = tf.compat.as_bytes("JFIF") in fobj.peek(10)
        finally:
            fobj.close()

        if not is_jfif:
            num_skipped += 1
            # Delete corrupted image
            os.remove(fpath)

print("Deleted %d images" % num_skipped)
