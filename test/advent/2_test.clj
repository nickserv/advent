(ns advent.2-test
  (:require [clojure.test :refer :all]
            [advent.2 :refer :all]))

(deftest process-opcodes-test
  (are [x y] (= x (process-opcodes y))
    [2 0 0 0 99] [1 0 0 0 99]
    [2 3 0 6 99] [2 3 0 3 99]
    [2 4 4 5 99 9801] [2 4 4 5 99 0]
    [30 1 1 4 2 5 6 0 99] [1 1 1 4 99 5 6 0 99]))
