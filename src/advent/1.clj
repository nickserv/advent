(ns advent.1
  (:require [clojure.string :as str]))

(def masses
  (map #(Integer/parseInt %)
       (str/split-lines (slurp "src/advent/input1.txt"))))

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
