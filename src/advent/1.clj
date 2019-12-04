(ns advent.1
  (:require [clojure.string :as str]
            [clojure.java.io :as io]))

(def masses
  (map #(Integer/parseInt %)
       (str/split-lines (slurp (io/resource "input1.txt")))))

(defn fuel [mass]
  (- (int (/ mass 3))
     2))

(defn additional-fuel [mass]
  (if (> (fuel mass) 0)
    (+ (fuel mass) (additional-fuel (fuel mass)))
    0))

(defn -main [& args]
  (println (reduce + (map fuel masses)))
  (println (reduce + (map additional-fuel masses))))
