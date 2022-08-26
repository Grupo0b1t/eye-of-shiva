from sklearn import tree

features = [

                [3, 2, 2, 1, 0], [2, 0, 15, 0, 0], [20, 3, 0, 0, 0], [0, 0, 2, 0, 0], [0, 0, 2, 0, 5], [0, 0, 0, 0, 0], [2, 2, 0, 0, 0], [0, 2, 0, 20, 0], [0, 2, 0, 2, 0], # [0] - Not Ransomware

                [3, 2, 2, 1, 8], [2, 0, 15, 0, 5], [11, 0, 0, 11, 0], [0, 10, 0, 2, 30], [2, 10, 3, 1, 0], [0, 40, 40, 0, 30] # [1] - Possible Ransomware

]

labels = [  0,0,0,0,0,0,0,0,0,  # [0] - Not Ransomware
            1,1,1,1,1,1   # [1] - Possible Ransomware
        ]   

classifying = tree.DecisionTreeClassifier()
classifying.fit(features, labels)

def evaluate(created_files, modified_files, moved_files, deleted_files, trapfiles_edited):

    monitor = classifying.predict([[created_files, modified_files, moved_files, deleted_files, trapfiles_edited]])

    if monitor == 0:

        pass

    elif monitor == 1:

        return True
