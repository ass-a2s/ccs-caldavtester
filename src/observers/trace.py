##
# Copyright (c) 2014-2016 Apple Inc. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
##

from src.observers.log import Observer as LogObserver


class Observer(LogObserver):
    """
    A results observer that prints results to standard output.
    """

    _print_details = True

    def updateCalls(self):
        super(Observer, self).updateCalls()
        self._calls.update({
            "trace": self.trace,
        })

    def trace(self, text, indent=0):
        self.manager.logit(text)
