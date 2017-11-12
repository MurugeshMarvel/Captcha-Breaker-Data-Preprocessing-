import tensorflow as tf

filename_queue = tf.train.string_input_producer(
    tf.train.match_filenames_once("/home/kratos/Documents/Office/OCR/csv/*.png"))
image_reader = tf.WholeFileReader()
_, image_file = image_reader.read(filename_queue)

image = tf.image.decode_png(image_file)

with tf.Session() as sess:
    tf.local_variables_initializer().run()

    coord = tf.train.Coordinator()
    threads = tf.train.start_queue_runners(coord=coord)

    image_tensor = sess.run([image])
    print(image_tensor)

    coord.request_stop()
    coord.join(threads)
