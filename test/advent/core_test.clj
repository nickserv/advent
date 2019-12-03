(ns advent.core-test
  (:require [clojure.test :refer :all]
            [advent.core :refer :all]))

(deftest fuel-test
  (are [x y] (= x (fuel y))
    2 12
    2 14
    654 1969
    33583 100756))

(deftest additional-fuel-test
  (are [x y] (= x (additional-fuel y))
    2 14
    966 1969
    50346 100756))

(deftest process-opcodes-test
  (are [x y] (= x (process-opcodes y))
    [2 0 0 0 99] [1 0 0 0 99]
    [2 3 0 6 99] [2 3 0 3 99]
    [2 4 4 5 99 9801] [2 4 4 5 99 0]
    [30 1 1 4 2 5 6 0 99] [1 1 1 4 99 5 6 0 99]))
