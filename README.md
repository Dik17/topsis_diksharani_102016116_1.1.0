# Topsis_Diksha_102016116
Topsis_Diksha_102016116 is a Python Package implementing [Topsis](https://www.sciencedirect.com/science/article/pii/S277266222100014X#:~:text=TOPSIS%20is%20based%20on%20the,distances%20from%20the%20ideal%20solutions.) method used for multi-criteria decision analysis.
Topsis stands for 'Technique for Order of Preference by Similarity to Ideal Solution'.

## Installation
Install the Package using the command - 
```s
$ pip install Topsis_Diksha_102016116
```
## Example
|Fund Name    P1    P2   P3    P4     P5  |
|-----------------------------------------|
|0        M1  0.81  0.66  7.0  57.6  16.52|    
|1        M2  0.69  0.48  5.4  60.7  16.82|     
|2        M3  0.76  0.58  3.5  40.8  11.41|     
|3        M4  0.74  0.55  3.1  66.8  17.80|    
|4        M5  0.80  0.64  5.9  53.3  15.16|    
|5        M6  0.95  0.90  3.8  62.8  17.11|    
|6        M7  0.81  0.66  3.0  32.6   9.27|    
|7        M8  0.62  0.38  4.2  51.9  14.28|    

weights : [1,1,1,1,1]
impacts : [+,-,+,-,+]

**input:** 102016116.csv
```s
python -m  Topsis_Diksha_102016116.topsis102016116 "C:\Users\Diksha\Downloads\102016116.csv" "1,1,1,1,1" "+,-,+,-,+" "C:\Users\Diksha\Downloads\102016116-result.csv"
```

**output:** 102016116-result.csv
|Fund Name   P1   P2  P3    P4     P5  Performance  Rank     |
|------------------------------------------------------------|
|0        M1  0.81  0.66  7.0  57.6  16.52     0.619058     1|
|1        M2  0.69  0.48  5.4  60.7  16.82     0.578429     2|
|2        M3  0.76  0.58  3.5  40.8  11.41     0.437109     5|
|3        M4  0.74  0.55  3.1  66.8  17.80     0.422480     6|
|4        M5  0.80  0.64  5.9  53.3  15.16     0.577352     3|
|5        M6  0.95  0.90  3.8  62.8  17.11     0.364704     8|
|6        M7  0.81  0.66  3.0  32.6   9.27     0.406832     7|
|7        M8  0.62  0.38  4.2  51.9  14.28     0.534840     4|


## License

MIT

**Free Software, Hell Yeah!**

## License

MIT

**Free Software, Hell Yeah!**
