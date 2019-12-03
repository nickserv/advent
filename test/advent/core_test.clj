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
