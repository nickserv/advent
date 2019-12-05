(ns advent.core
  (:require [advent.1]
            [advent.2]
            [advent.4])
  (:gen-class))

(defn -main [& args]
  (advent.1/-main)
  (advent.2/-main)
  (advent.4/-main))
