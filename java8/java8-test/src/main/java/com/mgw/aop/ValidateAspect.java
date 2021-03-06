package com.mgw.aop;

import org.aspectj.lang.JoinPoint;
import org.aspectj.lang.ProceedingJoinPoint;
import org.aspectj.lang.Signature;
import org.aspectj.lang.annotation.*;

import java.util.Arrays;

//@Component
@Aspect
//@Order(1) //使用此注解改变顺序
public class ValidateAspect {


    @Pointcut("execution(* com.mgw.aop.MyCaculator.*(..))")
    public void point() {}


    @Before("point()")
    public void logBefore(JoinPoint joinPoint) {

        Object[] args = joinPoint.getArgs();

        //获取方法签名
        Signature signature = joinPoint.getSignature();

        System.out.println("ValidateAspect切面前置["+signature.getName()+"]方法开始执行,参数列表是:"+ Arrays.asList(args));

    }

    @After("point()")
    public void logAfter(JoinPoint joinPoint) {

        Signature signature = joinPoint.getSignature();

        System.out.println("ValidateAspect切面后置["+signature.getName()+"]方法最终结束");

    }


    @AfterReturning(value = "point()",returning = "result")
    public void logReturn(JoinPoint joinPoint,Object result) {

        Signature signature = joinPoint.getSignature();


        System.out.println("ValidateAspect切面返回["+signature.getName()+"]方法正常执行完成,结果是:"+result);
    }

    @AfterThrowing(value = "point()",throwing = "e")
    public void logException(JoinPoint joinPoint,Exception e) {

        Signature signature = joinPoint.getSignature();

        System.out.println("ValidateAspect切面异常["+signature.getName()+"]方法发生异常,异常信息是:"+e.getMessage());
    }

//    @Around(value = "point()")
    public Object myAround(ProceedingJoinPoint proceedingJoinPoint) throws Throwable {

        Object[] args = proceedingJoinPoint.getArgs();
        Signature signature = proceedingJoinPoint.getSignature();
        Object result = null;

        try {

            //实际上就是method.invoke(obj,args)
            System.out.println("ValidateAspect切面环绕[环绕前置通知]"+signature.getName() +"方法开始");
            result = proceedingJoinPoint.proceed(args);
            System.out.println("环绕...");
            System.out.println("ValidateAspect切面环绕[环绕返回通知]"+signature.getName() +"方法返回,结果是:"+result);

        }catch (Exception e) {
            System.out.println("ValidateAspect切面环绕[环绕异常通知]"+signature.getName() +"方法异常,异常信息是:"+e.getMessage());
            throw new RuntimeException(e);

        }finally {
            System.out.println("ValidateAspect切面环绕[环绕后置通知]"+signature.getName() +"方法最终结束");
        }
        return result;
    }

}
