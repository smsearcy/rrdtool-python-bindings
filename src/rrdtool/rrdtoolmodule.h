#ifndef __RRDTOOLMODULE_H_
#define __RRDTOOLMODULE_H_

#include <rrd.h>

/* need rrd_format.h for some constants */
#define RRD_EXPORT_DEPRECATED
#include <rrd_format.h>

/* include graph functionality */
#define HAVE_RRD_GRAPH

/* `rrd_fetch_cb_register` is defined in headers included in distribution headers */
typedef int (*rrd_fetch_cb_t)(
    const char     *filename,  /* name of the rrd */
    enum cf_en     cf_idx, /* consolidation function */
    time_t         *start,
    time_t         *end,       /* which time frame do you want ?
                                * will be changed to represent reality */
    unsigned long  *step,      /* which stepsize do you want?
                                * will be changed to represent reality */
    unsigned long  *ds_cnt,    /* number of data sources in file */
    char           ***ds_namv, /* names of data_sources */
    rrd_value_t    **data      /* two dimensional array containing the data */
);
int rrd_fetch_cb_register(rrd_fetch_cb_t cb);

#endif /* __RRDTOOLMODULE_H_ */
