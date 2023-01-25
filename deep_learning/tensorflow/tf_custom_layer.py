import tensorflow as tf

#
# custom layer
#


class MyDenseLayer(tf.keras.layers.Layer):
    def __init__(self, num_outputs):
        super(MyDenseLayer, self).__init__()
        self.num_outputs = num_outputs

    def build(self, input_shape):
        self.kernel = self.add_weight(
            "kernel", shape=[int(input_shape[-1]), self.num_outputs]
        )

    def call(self, inputs):
        return tf.matmul(inputs, self.kernel)


layer = MyDenseLayer(10)
