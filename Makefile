.PHONY: lib run

lib:
	@echo "Installing libraries..."
	python3 setup.py install

run:
	@echo "Running interface..."
	python3 Loan_approval_prediction/GUI.py
