(ns advent.core
  (:require [advent.1]
            [advent.2])
  (:gen-class))

(defn -main [& args]
  (advent.1/-main)
  (advent.2/-main))
