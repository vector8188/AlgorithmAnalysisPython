def mergeSort(alist):
    print("Splitting, {}".format(alist))
    if len(alist) > 1:
        mid = len(alist) // 2
        leftHalf = alist[:mid]
        rightHalf = alist[mid:]

        mergeSort(leftHalf)
        mergeSort(rightHalf)
        print("leftHalf, {}".format(leftHalf))
        print("rightHalf, {}".format(rightHalf))
        leftHalfIdx = rightHalfIdx = counter = 0
        print("checking boundry conditions")
        while (leftHalfIdx < len(leftHalf) and rightHalfIdx < len(rightHalf)):
            print("boundry conditions passes")
            if leftHalf[leftHalfIdx] < rightHalf[rightHalfIdx]:
                print("{} < {}".format(leftHalf[leftHalfIdx], rightHalf[rightHalfIdx]))
                print("alist: {}".format(alist))
                print("therefore putting {} in place of {}".format(leftHalf[leftHalfIdx], alist[counter]))
                alist[counter] = leftHalf[leftHalfIdx]
                leftHalfIdx = leftHalfIdx + 1
            else:
                print("{} > {}".format(leftHalf[leftHalfIdx], rightHalf[rightHalfIdx]))
                print("alist: {}".format(alist))
                print("therefore putting {} in place of {}".format(rightHalf[rightHalfIdx], alist[counter]))
                alist[counter] = rightHalf[rightHalfIdx]
                rightHalfIdx = rightHalfIdx + 1
            counter = counter + 1

        while rightHalfIdx < len(rightHalf):
            print("alist: {} before reset".format(alist))
            print("looping over rightHalf {}".format(rightHalf))
            print("counter: {}".format(counter))
            alist[counter] = rightHalf[rightHalfIdx]
            print("alist: after reset {}".format(alist))
            rightHalfIdx = rightHalfIdx + 1
            counter = counter + 1

        while leftHalfIdx < len(leftHalf):
            print("alist: before reset {}".format(alist))
            print("looping over leftHalf {}".format(leftHalf))
            print("counter: {}".format(counter))
            alist[counter] = leftHalf[leftHalfIdx]
            print("alist: after reset {}".format(alist))
            leftHalfIdx = leftHalfIdx + 1
            counter = counter + 1
        print("\nboundry conditions fails")

    print("Merging, {}\n".format(alist))

alist = [54,26,93,17,77,31,44,55,20]
mergeSort(alist)
print(alist)