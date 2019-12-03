(ns advent.core
  (:gen-class))

(defn fuel [mass]
  (- (int (/ mass 3)) 2))

(defn -main [& args]
  (println (reduce +
                   (map #(fuel (Integer/parseInt %))
                        (clojure.string/split-lines (slurp "src/advent/input.txt"))))))
