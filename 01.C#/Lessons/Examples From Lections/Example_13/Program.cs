/*
int[,] pic = new int [,]
{
    {0, 0, 0,0 , 1, 0, 1 ,0 ,0}
    {0, 0, 0,0 , 1, 0, 1 ,0 ,0},
    {0, 0, 0,0 , 1, 0, 1 ,0 ,0},
    {0, 0, 0,0 , 1, 0, 1 ,0 ,0},
    {0, 0, 0,0 , 1, 0, 1 ,0 ,0},
    {0, 0, 0,0 , 1, 0, 1 ,0 ,0},
    {0, 0, 0,0 , 1, 0, 1 ,0 ,0},
    
}
/*
void PrintImage(int[,] image)
{
    for (int i = 0; i < image.GetLength(0); i++)
    {
        for (int j = 0; j < image.GetLength(1); j++)
        {
            //Console.Write($"{image[i, j]} ");
            if(image[i,j] == 0) Console.Write($" ");
            else Console.Write($"+");
        }
    Console.WriteLine();
    }

}
*/

/*void FIllImage(int row, int col)
{
    if(pic)[row, col] == 0)
    {
        pic[row,col] = 1;
        FIllImage(row-1,col);
        FIllImage(row, col-1);
        FIllImage(row+1,col);
        FIllImage(row, col+1);
    }
}
*/
PrintImage(pic);
FIllImage(13,13);
PrintImage(pic);