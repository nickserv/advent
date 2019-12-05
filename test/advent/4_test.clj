(ns advent.4-test
  (:require [clojure.test :refer :all]
            [advent.4 :refer :all]))

(deftest password?-test
  (is (password? 111111))
  (is (not (password? 223450)))
  (is (not (password? 123789))))
