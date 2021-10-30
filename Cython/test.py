import main
import time
start_vanilla = time.time()
main.prime_finder_vanilla(999999)
end_vanilla = time.time()

print(f"vanilla python: {end_vanilla-start_vanilla}")


start_c = time.time()
main.prime_finder_optimized(999999)
end_c = time.time()

print(f"cython: {end_c-start_c}")
