<script>
    $(document).ready(function() {
        $('[id^=id_probability], [id^=id_license_area], [id^=id_unit_rate]').on('input', function() {
            var licenseArea = parseFloat($(this).val());
            var unitRate = parseFloat($('#id_unit_rate_0').val());
            var probability = parseFloat($('#id_probability').val());
            console.log(probability);
            var estimatedValueFieldID = '[id^=id_estimated_value]'; // Updated to use attribute selector
            var estimatedWeightedValueFieldID = '[id^=id_weighted_value]'; // Updated to use attribute selector
            
            if (!isNaN(licenseArea) && !isNaN(unitRate)) {
                var estimatedValue = licenseArea * unitRate;                
                $(estimatedValueFieldID).val(estimatedValue.toFixed(2));
            }
            if (!isNaN(licenseArea) && !isNaN(unitRate)) {
                var prob = probability / 100;                
                var weightedValue = licenseArea * unitRate * prob;  
                $(estimatedWeightedValueFieldID).val(weightedValue.toFixed(2));
            }


        });
    });
</script>