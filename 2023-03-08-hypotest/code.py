import mitiq
from mitiq.zne.inference import LinearFactory
from mitq.zne.scaling import fold_global

circuit = ...
executor = ...
observable = ...
icm = ...
rule = ...


mitiq.zne.execute_with_zne(
    circuit,
    executor,
    factory=LinearFactory([1.0, 2.0, 3.0]),
    scale_noise=fold_global,
)

mitiq.rem.execute_with_rem(
    circuit,
    executor,
    observable,
    inverse_confusion_matrix=icm,
)

mitiq.ddd.execute_with_ddd(
    circuit,
    executor,
    rule=mitiq.ddd.rules.xx,
)
