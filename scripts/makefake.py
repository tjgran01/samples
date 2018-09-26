import os
import random
import numpy as np
import pandas as pd

from dataheadings import tlx as tlx

class FakeMaker(object):
    def __init__(self, data_dir, file_num=10, file_prefix="11", num_trials=10):
        self.data_headings = tlx
        self.data_dir = data_dir
        self.file_num = file_num
        self.file_prefix = file_prefix
        self.num_trials = num_trials
        self.file_names = self.make_file_names()
        self.data_to_write = self.make_fake_data()
        self.can_write = self.ensure_consistency()
        if self.can_write:
            self.write_files()


    def make_file_names(self):
        self.file_names = [f"{self.file_prefix}{id + 1}" for id in
                           range(0, self.file_num)]
        for idx, fname in enumerate(self.file_names):
            if len(fname) == 3:
                self.file_names.pop(idx)
                self.file_names.insert(idx, f"{fname[:2]}0{fname[2:]}")
        return self.file_names


    def make_fake_data(self):

        all_data = []
        for fname in self.file_names:
            data_set = []
            for x in range(self.num_trials):
                data = [random.randint(1, 21) for x in
                        range(len(self.data_headings))]
                data_set.append(data)
            all_data.append(data_set)
        return all_data


    def ensure_consistency(self):
        assert len(self.data_to_write) == len(self.file_names)
        return True


    def write_files(self):

        for idx, data in enumerate(self.data_to_write):
            df = pd.DataFrame(data=data, columns=self.data_headings)
            df.to_csv(f"{self.data_dir}{self.file_names[idx]}.csv", index=False)


fm = FakeMaker("../data/")
fm.ensure_consistency()
