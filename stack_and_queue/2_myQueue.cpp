/* ************************************************************************
> File Name:     2_myQueue.cpp
> Author:        xmw01
> Created Time:  Sun 14 May 2023 01:50:15 PM CST
> Description:   
 ************************************************************************/

/*
使用栈实现队列的下列操作：

push(x) -- 将一个元素放入队列的尾部。
pop() -- 从队列首部移除元素。
peek() -- 返回队列首部的元素。
empty() -- 返回队列是否为空

MyQueue queue = new MyQueue();
queue.push(1);
queue.push(2);
queue.peek();  // 返回 1
queue.pop();   // 返回 1
queue.empty(); // 返回 false

说明:

你只能使用标准的栈操作 -- 也就是只有 push to top, peek/pop from top, size, 和 is empty 操作是合法的。
你所使用的语言也许不支持栈。你可以使用 list 或者 deque（双端队列）来模拟一个栈，只要是标准的栈操作即可。
假设所有操作都是有效的 （例如，一个空的队列不会调用 pop 或者 peek 操作）

*/

#include<iostram>
#include<stack>

using namespace std;

class MyQueue
{
public:
    stack<int> stIn;
    stack<int> stOut;

    // push element x to the back of queue
    void push(int x){
        stIn.push(x);
    }

    // initailizate your data structure here
    MyQueue(){

    }

    // remove the element from in front of queue and return the element.
    int pop(){
        if(stOut.empty()){
            while(!stIn.empty()){
                stOut.push(stIn.top());
                stIn.pop();
            }
        }
        int result = stOut.top();
        stOut.pop();
        return result;
    }

    // get the front element
    int peek(){
        int res = this->pop();
        stOut.push(res);
        return res;
    }

    //retrun whether the queue is empty;
    bool empty(){
        return stIn.empty() &&stOut.empty();
    }

};









