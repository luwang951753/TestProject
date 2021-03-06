package com.mgw.jdbc;

import org.apache.ibatis.logging.log4j.Log4jImpl;
import org.mybatis.spring.SqlSessionFactoryBean;
import org.mybatis.spring.annotation.MapperScan;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.Configuration;
import org.springframework.context.annotation.PropertySource;
import org.springframework.core.env.Environment;
import org.springframework.jdbc.datasource.DriverManagerDataSource;

import javax.sql.DataSource;

@Configuration
@ComponentScan("com.mgw.jdbc")
@PropertySource(value = "classpath:/jdbc.properties")
@MapperScan("com.mgw.jdbc")
//@MyMapperScan
public class JdbcConfig {

	@Autowired
	private Environment env;

	public static final String JDBC_URL = "jdbc_url";
	public static final String JDBC_USERNAME = "jdbc_username";
	public static final String JDBC_PASSWORD = "jdbc_password";
	public static final String JDBC_DRIVER = "jdbc_driver";

	@Bean
	public DataSource dataSource() {

		//DriverManagerDataSource是spring-jdbc提供的一个链接池
		DriverManagerDataSource driverManagerDataSource = new DriverManagerDataSource();
		driverManagerDataSource.setUrl(env.getProperty(JDBC_URL));
		driverManagerDataSource.setDriverClassName(env.getProperty(JDBC_DRIVER));
		driverManagerDataSource.setUsername(env.getProperty(JDBC_USERNAME));
		driverManagerDataSource.setPassword(env.getProperty(JDBC_PASSWORD));

		return driverManagerDataSource;
	}

	/**
	 * mybatis的一级缓存与spring整合时 会失效
	 *
	 *
	 * */
	@Bean
	public SqlSessionFactoryBean sqlSessionFactoryBean() {

		//SqlSessionFactoryBean是mybatis-spring提供的
		SqlSessionFactoryBean sqlSessionFactoryBean = new SqlSessionFactoryBean();
		//添加日志系统
		org.apache.ibatis.session.Configuration configuration = new org.apache.ibatis.session.Configuration();
		configuration.setLogImpl(Log4jImpl.class);
		sqlSessionFactoryBean.setConfiguration(configuration);

		sqlSessionFactoryBean.setDataSource(dataSource());

		return sqlSessionFactoryBean;
	}

}
