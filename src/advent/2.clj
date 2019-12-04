(ns advent.2
  (:require [clojure.string :as str]
            [clojure.math.combinatorics :as combo]
            [clojure.java.io :as io]))

(def opcodes
  (map #(Integer/parseInt %)
       (str/split (str/trim (slurp (io/resource "2.txt"))) #",")))

(defn replace-opcodes [opcodes x y]
  (assoc (assoc opcodes 1 x) 2 y))

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

(defn find-parameters [opcodes output]
  (first (filter (fn [[x y]] (= output (first (process-opcodes (replace-opcodes opcodes x y)))))
                 (combo/selections (range 100) 2))))

(defn -main [& args]
  (println (first (process-opcodes (replace-opcodes (vec opcodes) 12 2))))
  (println (let [[x y] (find-parameters (vec opcodes) 19690720)]
             (+ (* 100 x) y))))
