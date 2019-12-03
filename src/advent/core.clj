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
  (let [opcode (get opcodes position)
        left (get opcodes (+ 1 position))
        right (get opcodes (+ 2 position))
        result (get opcodes (+ 3 position))
        new-position (+ 4 position)]
    (if (some #{opcode} [1 2])
      (process-opcodes (assoc opcodes result ((if (= 1 opcode) + *)
                                              (get opcodes left)
                                              (get opcodes right)))
                       new-position)
      opcodes)))

(defn -main [& args]
  (println (reduce + (map fuel masses)))
  (println (reduce + (map additional-fuel masses))))
