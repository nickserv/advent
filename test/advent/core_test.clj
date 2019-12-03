(ns advent.core-test
  (:require [clojure.test :refer :all]
            [advent.core :refer :all]))

(deftest fuel-test
  (is (= 2 (fuel 12)))
  (is (= 2 (fuel 14)))
  (is (= 654 (fuel 1969)))
  (is (= 33583 (fuel 100756))))

(deftest additional-fuel-test
  (is (= 2 (additional-fuel 14)))
  (is (= 966 (additional-fuel 1969)))
  (is (= 50346 (additional-fuel 100756))))
