### How to use
You can run this script by using following commands.

    - start staircase sweep measurement using Keithley 6517B
        uv run python src/run.py (start voltage) (end voltage) (step size)
        example: uv run python src/run.py -0.2 -1.0, -0.05
    
    - acquire data from the instrument
        uv run python get.py
        the data will be saved as csv file.