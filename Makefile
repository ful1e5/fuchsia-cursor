all: clean render build

unix: clean render bitmaps
	@cd builder && make build_unix

windows: clean render bitmaps
	@cd builder && make build_windows

.PHONY: all

clean:
	@rm -rf bitmaps themes
	
render: bitmapper svg
	@cd bitmapper && $(MAKE)

build: bitmaps
	@cd builder && make setup build

.ONESHELL:
SHELL:=/bin/bash


src = ./themes/Fuchsia*
local := ~/.icons
local_dest := $(local)/Fuchsia*

root := /usr/share/icons
root_dest := $(root)/Fuchsia*

install: $(src)
	@if [[ $EUID -ne 0 ]]; then
		@echo "> Installing 'Fuchsia' cursors inside $(local)/..."
		@mkdir -p $(local)
		@cp -r $(src) $(local)/ && echo "> Installed!"
	@else
		@echo "> Installing 'Fuchsia' cursors inside $(root)/..."
		@mkdir -p $(root)
		@sudo cp -r $(src) $(root)/ && echo "> Installed!"
	@fi

uninstall:
	@if [[ $EUID -ne 0 ]]; then
		@echo "> Removing 'Fuchsia' cursors from '$(local)'..."
		@rm -rf $(local_dest)
	@else
		@echo "> Removing 'Fuchsia' cursors from '$(root)'..."
		@sudo rm -rf $(root_dest)
	@fi

reinstall: uninstall install

# generates binaries
BIN_DIR = ../bin
THEMES = Pop!
prepare: bitmaps themes
	# bitmaps
	@rm -rf bin && mkdir bin
	@cd bitmaps && zip -r $(BIN_DIR)/bitmaps.zip * && cd ..
	# themes
	@cd themes
	@tar -czvf $(BIN_DIR)/Fuchsia.tar.gz Fuchsia
	@zip -r $(BIN_DIR)/Fuchsia-Windows.zip Fuchsia-Windows
	@$(foreach theme,$(THEMES), tar -czvf $(BIN_DIR)/Fuchsia-$(theme).tar.gz Fuchsia-$(theme);)
	@$(foreach theme,$(THEMES), zip -r $(BIN_DIR)/Fuchsia-$(theme)-Windows.zip Fuchsia-$(theme)-Windows;)
	@cd ..
