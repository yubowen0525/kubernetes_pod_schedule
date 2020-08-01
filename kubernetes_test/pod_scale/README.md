# Pod的扩缩容 Scale机制
- 手动：通过执行kubectl scale或者通过RESTful API对一个Deployment/RC进行Pod副本数量设置。
- 自动：用户根据某个性能指标或者自定义业务指标，指定Pod副本数量范围

## 手动 
可大可小，扩杀
```
kubectl scale deployment [name] --replicas 5
```

## 自动HPA
- 首先Pod 需要定义 Pod Request的值，才能使用CPUUtilizationPercentage
- Kubernetes Monitoring Architecture 中 定义一套标准化API接口 Resource Metrics API

### 算法详解
