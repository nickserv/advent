(ns advent.core
  (:gen-class))

(def masses
  (map #(Integer/parseInt %)
       (clojure.string/split-lines (slurp "src/advent/input.txt"))))

(defn fuel [mass]
  (- (int (/ mass 3))
     2))

(defn additional-fuel [mass]
  (if (> (fuel mass) 0)
    (+ (fuel mass) (additional-fuel (fuel mass)))
    0))

(def opcodes
  (map #(Integer/parseInt %)
       (clojure.string/split (clojure.string/trim (slurp "src/advent/input2.txt")) #",")))

(defn process-opcodes [opcodes position]
  (cond
    (= 1 (get opcodes position)) (process-opcodes (assoc opcodes
                                                         (get opcodes (+ 3 position))
                                                         (+ (get opcodes (get opcodes (+ 1 position)))
                                                            (get opcodes (get opcodes (+ 2 position)))))
                                                  (+ 4 position))
    (= 2 (get opcodes position)) (process-opcodes (assoc opcodes
                                                         (get opcodes (+ 3 position))
                                                         (* (get opcodes (get opcodes (+ 1 position)))
                                                            (get opcodes (get opcodes (+ 2 position)))))
                                                  (+ 4 position))
    :else opcodes))

(defn -main [& args]
  (println (reduce + (map fuel masses)))
  (println (reduce + (map additional-fuel masses))))
