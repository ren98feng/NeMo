# Copyright (c) 2020, NVIDIA CORPORATION.  All rights reserved.
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

from typing import Dict

import torch
from pytorch_lightning.metrics import Metric

from nemo.utils import logging

__all__ = ['Perplexity']


class Perplexity(Metric):
    """
    This metric computes the perplexity given the language model loss.
    """

    def __init__(self, dist_sync_on_step=False):
        super().__init__(dist_sync_on_step=dist_sync_on_step)
        self.add_state('perplexity', default=torch.tensor(0), dist_reduce_fx='mean', persistent=False)

    def update(self, loss: torch.Tensor):
        self.perplexity = torch.exp(loss)

    def compute(self):
        return self.perplexity
