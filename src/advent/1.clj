(ns advent.1
  (:require [clojure.string :as str]
            [clojure.java.io :as io]))

(def masses
  (map read-string (str/split-lines (slurp (io/resource "1.txt")))))

(defn fuel [mass]
  (- (int (/ mass 3))
     2))

(defn additional-fuel [mass]
  (if (pos? (fuel mass))
    (+ (fuel mass) (additional-fuel (fuel mass)))
    0))

(defn -main [& args]
  (println (reduce + (map fuel masses)))
  (println (reduce + (map additional-fuel masses))))
