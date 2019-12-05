(ns advent.4
  (:require [clojure.string :as str]))

(defn adjacent? [xs]
  (and (not (nil? (second xs)))
       (or (= (first xs) (second xs))
           (recur (rest xs)))))

(defn increasing? [xs]
  (or (nil? (second xs))
      (and (<= (first xs) (second xs))
           (recur (rest xs)))))

(defn password? [x]
  (let [xs (map read-string (str/split (str x) #""))]
    (and (adjacent? xs)
         (increasing? xs))))

(defn -main [& args]
  (println (count (filter password? (range 402328 (inc 864247))))))
