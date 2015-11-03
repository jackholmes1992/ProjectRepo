#include <sys/types.h>
#include <errno.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>
#include <iostream>
#include <cstdlib>
using namespace std;

int main(void)
{
	execlp("", "wc", "-w", NULL);
}











