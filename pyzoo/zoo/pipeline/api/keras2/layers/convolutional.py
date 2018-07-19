#
# Copyright 2018 Analytics Zoo Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import sys
from zoo.pipeline.api.keras2.base import ZooKeras2Layer

if sys.version >= '3':
    long = int
    unicode = str


class Conv1D(ZooKeras2Layer):
    """1D convolution layer (e.g. temporal convolution).

    This layer creates a convolution kernel that is convolved
    with the layer input over a single spatial (or temporal) dimension
    to produce a tensor of outputs.
    If `use_bias` is True, a bias vector is created and added to the outputs.
    Finally, if `activation` is not `None`,
    it is applied to the outputs as well.

    When using this layer as the first layer in a model,
    provide an `input_shape` argument
    (tuple of integers or `None`, e.g.
    `(10, 128)` for sequences of 10 vectors of 128-dimensional vectors,
    or `(None, 128)` for variable-length sequences of 128-dimensional vectors.

    # Arguments
        filters: Integer, the dimensionality of the output space
            (i.e. the number of output filters in the convolution).
        kernel_size: An integer or tuple/list of a single integer,
            specifying the length of the 1D convolution window.
        strides: An integer or tuple/list of a single integer,
            specifying the stride length of the convolution.
            Specifying any stride value != 1 is incompatible with specifying
            any `dilation_rate` value != 1.
        padding: One of `"valid"`, `"causal"` or `"same"` (case-insensitive).
            `"valid"` means "no padding".
            `"same"` results in padding the input such that
            the output has the same length as the original input.
            `"causal"` results in causal (dilated) convolutions, e.g. output[t]
            does not depend on input[t+1:]. Useful when modeling temporal data
            where the model should not violate the temporal order.
        activation: Activation function to use
            (see [activations](../activations.md)).
            If you don't specify anything, no activation is applied
            (ie. "linear" activation: `a(x) = x`).
        use_bias: Boolean, whether the layer uses a bias vector.
        kernel_initializer: Initializer for the `kernel` weights matrix
        bias_initializer: Initializer for the bias vector
        kernel_regularizer: Regularizer function applied to
            the `kernel` weights matrix
        bias_regularizer: Regularizer function applied to the bias vector

    # Input shape
        3D tensor with shape: `(batch_size, steps, input_dim)`

    # Output shape
        3D tensor with shape: `(batch_size, new_steps, filters)`
        `steps` value might have changed due to padding or strides.

    >>> conv1d = Conv1D(12, 4, input_shape=(3, 16))
    creating: createZooKeras2Conv1D
    """
    def __init__(self,
                 filters,
                 kernel_size,
                 strides=1,
                 padding="valid",
                 activation=None,
                 use_bias=True,
                 kernel_initializer="glorot_uniform",
                 bias_initializer="zero",
                 kernel_regularizer=None,
                 bias_regularizer=None,
                 input_shape=None, **kwargs):
        super(Conv1D, self).__init__(None,
                                     filters,
                                     kernel_size,
                                     strides,
                                     padding,
                                     activation,
                                     use_bias,
                                     kernel_initializer,
                                     bias_initializer,
                                     kernel_regularizer,
                                     bias_regularizer,
                                     list(input_shape) if input_shape else None,
                                     **kwargs)


class Cropping1D(ZooKeras2Layer):
    """
    Cropping layer for 1D input (e.g. temporal sequence).
    The input of this layer should be 3D.

    When you use this layer as the first layer of a model, you need to provide the argument
    input_shape (a shape tuple, does not include the batch dimension).

    # Arguments
    cropping: Int tuple of length 2. How many units should be trimmed off at the beginning and
              end of the cropping dimension. Default is (1, 1).
    input_shape: A shape tuple, not including batch.
    name: String to set the name of the layer.
          If not specified, its name will by default to be a generated string.

    >>> cropping1d = Cropping1D(cropping=(1, 2), input_shape=(8, 8))
    creating: createZooKeras2Cropping1D
    """
    def __init__(self, cropping=(1, 1), input_shape=None, **kwargs):
        super(Cropping1D, self).__init__(None,
                                         cropping,
                                         list(input_shape) if input_shape else None,
                                         **kwargs)


class ZeroPadding1D(ZooKeras2Layer):
    """
    Zero-padding layer for 1D input (e.g. temporal sequence).
    The input of this layer should be 3D.

    When you use this layer as the first layer of a model, you need to provide the argument
    input_shape (a shape tuple, does not include the batch dimension).

    # Arguments
    padding: Int or int tuple of length 2.
             If int, how many zeros to add both at the beginning and at the end of
             the padding dimension.
             If tuple of length 2, how many zeros to add in the order '(left_pad, right_pad)'.
             Default is 1.
    input_shape: A shape tuple, not including batch.
    name: String to set the name of the layer.
          If not specified, its name will by default to be a generated string.

    >>> zeropadding1d = ZeroPadding1D(padding=2, input_shape=(3, 6))
    creating: createZooKeras2ZeroPadding1D
    """
    def __init__(self,
                 padding=1,
                 input_shape=None,
                 **kwargs):
        if isinstance(padding, int):
            padding = (padding, padding)
        super(ZeroPadding1D, self).__init__(None,
                                            padding,
                                            list(input_shape) if input_shape else None,
                                            **kwargs)


class ZeroPadding2D(ZooKeras2Layer):
    """
    Zero-padding layer for 2D input (e.g. picture).
    The input of this layer should be 4D.

    When you use this layer as the first layer of a model, you need to provide the argument
    input_shape (a shape tuple, does not include the batch dimension).

    # Arguments
    padding: Int tuple of length 2 or length 4.
             If tuple of length 2, how many zeros to add both at the beginning and
             at the end of rows and cols.
             If tuple of length 4, how many zeros to add in the order
             '(top_pad, bottom_pad, left_pad, right_pad)'.
             Default is (1, 1).
    data_format: Format of input data. Either 'channels_first' or 'channels_last'.
                  Default is 'channels_first'.
    input_shape: A shape tuple, not including batch.
    name: String to set the name of the layer.
          If not specified, its name will by default to be a generated string.

    >>> zeropadding2d = ZeroPadding2D(padding=(2, 1), input_shape=(2, 8, 8))
    creating: createZooKeras2ZeroPadding2D
    """
    def __init__(self,
                 padding=(1, 1),
                 data_format="channels_first",
                 input_shape=None, **kwargs):
        if len(padding) == 2:
            padding = (padding[0], padding[0], padding[1], padding[1])
        super(ZeroPadding2D, self).__init__(None,
                                            padding,
                                            data_format,
                                            list(input_shape) if input_shape else None,
                                            **kwargs)
