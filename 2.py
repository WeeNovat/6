        self.slider.valueChanged.connect(self.progress.setValue)

        self.slider.valueChanged.connect(
            lambda val: self.label.setText(f"Значення: {val}%")
        )

        self.check.stateChanged.connect(
            lambda state: self.btn.setEnabled(state == 2) 
        )

        self.reset_btn = QPushButton("Скинути")
        self.reset_btn.clicked.connect(self.reset_form)
        main_layout.addWidget(self.reset_btn)

    def reset_form(self):
        self.input_field.clear()
        self.slider.setValue(0)
        self.check.setChecked(False)
