package main

import (
	"log"
	"os"
	"runtime"
	"strconv"
)

func runMachine(sc <-chan int, victory chan<- int) {
	for {
		s := <- sc
		until := s + 10000
		for i := s; i < until; i++ {
			if (i / 10000) % 10 == 0 {
				i += 9999
				continue
			}
			if (i / 1000) % 10 == 0 {
				i += 999
				continue
			}
			if (i / 100) % 10 == 0 {
				i += 99
				continue
			}
			if (i / 10) % 10 == 0 {
				i += 9
				continue
			}
			if i % 10 == 0 {
				continue
			}
			z := runProgram(i)
			if z == 0 {
				log.Printf("Found it! %d.\n", i)
				victory <- i
			}
		}
	}
}

func blockThing(w, z, A, B, C int) int {
	var x, y int
	x = z % 26 + B
	z /= A
	if x == w {
		x = 0
	} else {
		x = 1
	}
	y = (25 * x) + 1
	z *= y
	y = (w + C) * x
	z += y
	return z
}
var z19 = blockThing(9, 0, 1, 11, 8)

func runProgram(input int) int {
	z := blockThing((input/10000000000000)%10, 0, 1, 11, 8)
	z = blockThing((input/1000000000000)%10, z, 1, 14, 13)
	z = blockThing((input/100000000000)%10, z, 1, 10, 2)
	z = blockThing((input/10000000000)%10, z, 26, 0, 7)
	z = blockThing((input/1000000000)%10, z, 1, 12, 11)
	z = blockThing((input/100000000)%10, z, 1, 12, 4)
	z = blockThing((input/10000000)%10, z, 1, 12, 13)
	z = blockThing((input/1000000)%10, z, 26, -8, 13)
	z = blockThing((input/100000)%10, z, 26, -9, 10)
	z = blockThing((input/10000)%10, z, 1, 11, 1)
	z = blockThing((input/1000)%10, z, 26, 0, 2)
	z = blockThing((input/100)%10, z, 26, -5, 14)
	z = blockThing((input/10)%10, z, 26, -6, 6)
	z = blockThing(input%10, z, 26, -12, 14)
	return z
}

func main() {
	threads := runtime.NumCPU()
	start, _ := strconv.Atoi(os.Args[1])
	log.Printf("Starting at %d.\n", start)
	sc := make(chan int, threads)
	victory := make(chan int)
	for i := 0; i < threads; i++ {
		go runMachine(sc, victory)
	}
	mainLoop:
	for i := start; ; i += 10000 {
		if (i / 10000000000000) % 10 == 0 {
			i += 9999999990000
			continue
		}
		if (i / 1000000000000) % 10 == 0 {
			i += 999999990000
			continue
		}
		if (i / 100000000000) % 10 == 0 {
			i += 99999990000
			continue
		}
		if (i / 10000000000) % 10 == 0 {
			i += 9999990000
			continue
		}
		if (i / 1000000000) % 10 == 0 {
			i += 999990000
			continue
		}
		if (i / 100000000) % 10 == 0 {
			i += 99990000
			continue
		}
		if (i / 10000000) % 10 == 0 {
			i += 9990000
			continue
		}
		if (i / 1000000) % 10 == 0 {
			i += 990000
			continue
		}
		if (i / 100000) % 10 == 0 {
			i += 90000
			continue
		}
		sc <- i
		select {
		case result := <- victory:
			log.Printf("Victory! %d.\n", result)
			break mainLoop
		default:
		}
		if i % 100000000 == 11111111 {
			log.Printf("s = %d\n", i)
		}
	}
}
