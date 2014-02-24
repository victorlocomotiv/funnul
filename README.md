# funnul

funnul turns nginx into a layer 7 edge router, with a sleek interface on top and REST API below.

## Feature Roadmap

Planned features, in no particular order:

- Dynamic proxy_pass / upstream configuration
- Weighted upstreams with % traffic control
- Support for blue green deploys, canary deploys, and orchestrated configuration
- Layer 7 rewrite rules
- Selective header injection (request)
- Selective header injection (response)
- Response cache rules
- nginx config testing
- SSL termination and certificate deployment
- Export configuration to git for change management

## Configuration Primitives

The primary configuration primitive is an application, which includes a hostname, one or more backends, and zero or more advanced routing rules. Configuration looks approximately like this:

    app: myapp.example.com
    backends:
      - group1: (80%)
        - backend1.example.com
        - backend2.example.com
      - group2 (20%)
        - backend3.example.com
    rules:
      - rewrite / -> /en/
      - add 24 hour cache headers to *.css
      - add 24 hour cache headers to *.js
      - add 30 day cache headers to *.jpg
      - requires SSL

Additional details will be added / clarified as the implementation develops.

## Implementation Details

The API and configuration app are written in Flask. The service tier *may* use etcd and confd to manage nginx. Chef deploy scripts will be included.