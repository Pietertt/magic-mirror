SOURCE_FILES = test.cpp
OUTPUT_DIR = bin
OUTPUT_FILES = $(OUTPUT_DIR)/main.o

compile:
	@g++ -std=c++11 $(SOURCE_FILES) -o $(OUTPUT_FILES) 

run:
	@make compile
	@./$(OUTPUT_FILES)