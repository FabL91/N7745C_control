def saveOneValue(self):
        # Adding the values to the lists
        self.sample_values = {}
        self.sample_values["power_sample"] = self.power_sample
        self.sample_values["lum_sample"] = self.luminance_sample
        self.sample_values["lum_fit"] = self.luminance_fit
        self.sample_values["residuals"] = self.residuals
        self.sample_values["residuals_%"] = self.residualspercent        
        self.sample_values["temperature"] = self.fit_T
        self.sample_values["epsilon"] = self.fit_epsilon 
        self.sample_values["timeSample"] = window.t0
        self.sample_values["all_power_sample"] = self.all_temp_values

        # Convert self.all_temp_values to a DataFrame for better handling
        all_temp_values_df = pd.DataFrame(self.all_temp_values).transpose()
        all_temp_values_df.columns = [f"all_power_sample_{i+1}" for i in range(all_temp_values_df.shape[1])]

        # Save the main values into a JSON file
        window.saveJson(self.sample_values, "sample_values" + window.t0, 'w+')

        # Load the saved JSON for consistency
        dfOnesample = pd.read_json(window.cdir + "sample_values" + window.t0 + ".json")  # Separating JSON into a DataFrame

        # Merge all_temp_values_df with the other data
        dfOnesample = pd.concat([dfOnesample, all_temp_values_df], axis=1)

        # Generate fieldnames dynamically
        fieldnames = list(self.sample_values.keys()) + list(all_temp_values_df.columns)

        # Save as CSV
        dfOnesample.to_csv(
            window.cdir + "sample_values" + window.t0 + ".csv",
            index=False,
            header=fieldnames,
            sep=';'
        )