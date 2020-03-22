package com.poplar.bytecode;

/**
 *
 * 静态分派的演示与证明：
 */
public class StaticDispatch {

    static abstract class Human {

    }

    static class Man extends Human {

    }

    static class Woman extends Human {

    }

    public void hello(Human param) {
        System.out.println("Hello Human");
    }

    public void hello(Man param) {
        System.out.println("Hello Man");
    }

    public void hello(Woman param) {
        System.out.println("Hello Woman");
    }

    public static void main(String[] args) {
        StaticDispatch dispatch = new StaticDispatch();
        Human man = new Man();
        Human woMan = new Woman();
        //静态分派，重载是在编译器即确定
        dispatch.hello(man);//Hello Human
        dispatch.hello(woMan);//Hello Human

        Human human = new Woman();
        human = new Man();
        dispatch.hello((Woman) human);
        dispatch.hello((Man) human);
        //java.lang.ClassCastException: main.java.com.poplar.bytecode.WoMan cannot be cast to main.java.com.poplar.bytecode.Man
    }
}
