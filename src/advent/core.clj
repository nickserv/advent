(ns advent.core
  (:require [clojure.string :as str])
  (:gen-class))

(def masses
  (map #(Integer/parseInt %)
       (str/split-lines (slurp "src/advent/input.txt"))))

(defn fuel [mass]
  (- (int (/ mass 3))
     2))

(defn additional-fuel [mass]
  (if (> (fuel mass) 0)
    (+ (fuel mass) (additional-fuel (fuel mass)))
    0))

(def opcodes
  (map #(Integer/parseInt %)
       (str/split (str/trim (slurp "src/advent/input2.txt")) #",")))

(defn replace-opcodes [opcodes first second]
  (assoc (assoc opcodes 1 first) 2 second))

(def operations (hash-map 1 + 2 *))

(defn process-opcodes
  ([opcodes]
   (process-opcodes opcodes 0))
  ([opcodes position]
   (let [operation (get operations (get opcodes position))
         left (get opcodes (get opcodes (+ 1 position)))
         right (get opcodes (get opcodes (+ 2 position)))
         result (get opcodes (+ 3 position))
         new-position (+ 4 position)]
     (if operation
       (recur (assoc opcodes result (operation left right)) new-position)
       opcodes))))

(defn -main [& args]
  (println (reduce + (map fuel masses)))
  (println (reduce + (map additional-fuel masses)))
  (println (first (process-opcodes (replace-opcodes (vec opcodes) 12 2)))))
