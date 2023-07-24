import os

class DatasetItem(list):
    def __init__(self, dataset_name, dataset_items=None):
        self.name = None
        # If the dataset_name is a DatasetItem object, copy its attributes to this object
        if isinstance(dataset_name, DatasetItem):
            self.dataset_name = dataset_name.dataset_name
            self.name = dataset_name.name

            # Append all the items in dataset_items to this object
            for d in dataset_items:
                self.append(d)
        else:
            # Initialize a list object
            super().__init__()

            # If the dataset_name is a list, set dataset_items to dataset_name
            if isinstance(dataset_name, list):
                dataset_items = dataset_name
                dataset_name = "Unnamed_Dataset"

            # If the dataset_name is a valid file path, set dataset_name to the basename of the file path
            if os.path.exists(dataset_name):
                while dataset_name and dataset_name[-1] in ["/", "\\"]:
                    dataset_name = dataset_name[:-1]
                self.dataset_name = os.path.basename(dataset_name)
            else:
                # Set the dataset_name to the given value
                self.dataset_name = dataset_name

            # If dataset_items is None, set it to dataset_name
            if not dataset_items:
                dataset_items = dataset_name

            # Append the dataset_items to this object
            if not isinstance(dataset_items, list):
                self.append(dataset_items)
            else:
                for d in dataset_items:
                    self.append(d)

            # Set the name attribute to the dataset_name
            self.name = self.dataset_name

    def __str__(self):
        return self.name
    
    
class ACOSDatasetList(list):
    Laptop14 = DatasetItem("Laptop14", "501.Laptop14")

    Restaurant14 = DatasetItem("Restaurant14", "502.Restaurant14")
    Restaurant15 = DatasetItem("Restaurant15", "503.Restaurant15")
    Restaurant16 = DatasetItem("Restaurant16", "504.Restaurant16")

    Chinese_Zhang = DatasetItem("Chinese_Zhang", "505.Chinese_Zhang")

    Synthetic = DatasetItem("Synthetic", "506.Synthetic")

    def __init__(self):
        super(ACOSDatasetList, self).__init__(
            [
                self.Laptop14,
                self.Restaurant14,
                self.Restaurant15,
                self.Restaurant16,
                # self.Chinese_Zhang,
                # self.Synthetic,
            ]
        )

