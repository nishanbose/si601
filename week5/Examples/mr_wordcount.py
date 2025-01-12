#!/usr/bin/python
# Copyright 2009-2010 Yelp
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

# Modified by Dr. Yuhang Wang for SI601
# To run locally:
# python mr_wordcount.py pg1268.txt > wordcount_output

"""The classic example of MapReduce job: count the frequency of words in file(s).
"""
from mrjob.job import MRJob
import re

WORD_RE = re.compile(r"\b[\w']+\b")

class MRWordFreqCount(MRJob):

    def mapper(self, _, line):
        for word in WORD_RE.findall(line):
            yield (word.lower(), 1)

    def reducer(self, word, countsgen):
        yield (word, sum(countsgen))


if __name__ == '__main__':
    MRWordFreqCount.run()